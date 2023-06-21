import pytest
from agbenchmark.challenges.retrieval.Retrieval import RetrievalChallenge
from agbenchmark.challenges.define_task_types import Challenge, Ground
import os

data = Challenge.deserialize(os.path.join(os.path.dirname(__file__), "r1_data.json"))


class TestRetrieval1(RetrievalChallenge):
    """The first information-retrieval challenge"""

    @pytest.mark.parametrize(
        "server_response",
        [data.task],
        indirect=True,
    )
    @pytest.mark.retrieval
    def test_retrieval(self, workspace):
        file = self.open_file(workspace, data.ground.files[0])

        score = self.scoring(file, data.ground)

        print("You score is:", score)

        assert score