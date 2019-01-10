import itertools
from typing import List, Union


def _slice_to_list(slice_: slice) -> List[int]:
    step = 1 if slice_.step is None else slice_.step
    return list(range(slice_.start, slice_.stop, step))


def _is_int(maybe_int):
    try:
        return int(maybe_int) == maybe_int
    except TypeError:
        pass
    return False


def frame_idx_to_list(frames_idx: Union[slice, List[slice], List[int]]) -> List[int]:
    """
    Converts a frame_idx object to a list of indices. Useful for testing.

    Args:
        frames_idx: Frame indices represented as a slice, list of slices, or list of
            ints.

    Returns:
        frame idx as a list of ints.

    """
    if isinstance(frames_idx, list):
        if isinstance(frames_idx[0], slice):
            return list(
                itertools.chain.from_iterable([_slice_to_list(s) for s in frames_idx])
            )
        if _is_int(frames_idx[0]):
            return frames_idx
    if isinstance(frames_idx, slice):
        return _slice_to_list(frames_idx)
    raise ValueError(
        "Can't handle {} objects, must be slice, List[slice], or List[int]".format(
            type(frames_idx)
        )
    )


def compute_sample_length(clip_length, step_size):
    """Computes the number of frames to be sampled for a clip of length
    ``clip_length`` with frame step size of ``step_size`` to be generated.

    Args:
        clip_length: Number of frames to sample
        step_size: Number of frames to skip in between adjacent frames in the output

    Returns:
        Number of frames to sample to read a clip of length ``clip_length`` while
        skipping ``step_size - 1`` frames.

    """
    return 1 + step_size * (clip_length - 1)
