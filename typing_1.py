from typing import Union, Optional, Tuple, Callable

def test_unpack(input_val: list[str], index: int) -> Tuple[str, int]:
    return (input_val[index], index)

result = test_unpack(2, 0)
print(result)
