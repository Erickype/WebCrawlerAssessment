from dataclasses import dataclass

@dataclass
class HackerNewsEntry:
    rank: int
    title: str
    points: int
    comments: int
