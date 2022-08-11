import pytest
from numpy.testing import assert_allclose

from mdakit_cookie.analysis.MyAnalysisClass import MyAnalysisClass
from mdakit_cookie.tests.utils import make_Universe

class TestMyAnalysisClass:
    
    # fixtures are helpful functions that set up a test
    # See more at https://docs.pytest.org/en/stable/how-to/fixtures.html
    @pytest.fixture
    def universe(self):
        u = make_Universe(
            extras=("names", "resnames",),
            n_frames=3,
        )
        # create toy data to test assumptions
        for ts in u.trajectory.ts:
            ts.positions[:ts.frame] *= -1
        return u

    @pytest.fixture
    def analysis(self, universe):
        return MyAnalysisClass(universe)


    @pytest.mark.parametrize(
        "select, n_atoms",  # argument names
        [  # argument values in a tuple, in order
            ("all", 125),
            ("index < 10", 10),
            ("resindex > 2", 50),
        ]
    )
    def test_atom_selection(self, universe, select, n_atoms):
        # `universe` here is the fixture defined above
        analysis = MyAnalysisClass(universe, select=select)
        assert analysis.atomgroup.n_atoms == n_atoms
    

    @pytest.mark.parametrize(
        "stop, expected_mean",
        [
            (0, 0),
            (1, 1),
            (2, 1.5),
        ]
    )
    def test_mean_negative_atoms(self, analysis, stop, expected_mean):
        # assert we haven't run yet and the result doesn't exist yet
        assert "mean_negative_atoms" not in analysis.results
        analysis.run(stop=stop)
        # when comparing floating point values, it's best to use assert_allclose
        # to allow for floating point precision differences
        assert_allclose(
            analysis.results.mean_negative_atoms,  # computed data
            expected_mean,  # reference / desired data
            rtol=1e-07, # relative tolerance
            atol=0, # absolute tolerance
            err_msg="mean_negative_atoms is not correct",
        )
