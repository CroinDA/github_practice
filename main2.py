from typing import Union, Optional


def add(
    x: Union[int, float], y: Union[int, float]
) -> Optional[
    Union[int, float]
]:  # x, y는 정수나 실수로 입력, 출력도 정수나 실수로 출력
    try:
        result = x + y
    except Exception as e:
        print(e)
        return None

    return result


if __name__ == "__main__":
    print(add(1, 2))
    print(add(1.5, 2.5))
    print(add(1, 2.5))
    print(add(1.5, 7))
