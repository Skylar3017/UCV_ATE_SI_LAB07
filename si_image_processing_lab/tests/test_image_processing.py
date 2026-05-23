import os

from si_image_processing_lab.pipelines.image_processing.nodes import (
    process_image,
)


def test_process_image():

    output_path = "data/03_primary/test_output.jpg"

    result = process_image(
        "data/01_raw/marte.jpg",
        output_path,
    )

    assert result is not None

    assert os.path.exists(output_path)