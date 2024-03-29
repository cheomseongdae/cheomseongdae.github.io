"""cheomseongdae"""
import sys


class Cheomseongdae:
    """첨성대"""

    @staticmethod
    def ping(n=1) -> str:
        """ping & pong

        To use:

            >>> Cheomseongdae.ping()
            pong

            >>> Cheomseongdae.ping(n=10)
            ppppppppppong

        Args:
            n: p 의 반복 횟수

        Returns:
            pong
        """
        return f"{'p' * n}ong"


def cmd_ping():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        r = Cheomseongdae.ping(n=n)
    else:
        r = Cheomseongdae.ping()

    print(r)

