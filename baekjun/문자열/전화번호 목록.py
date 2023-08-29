import sys
from collections import defaultdict

"""
백준 5052 전화번호 목록 (골드 4) - 트라이
https://www.acmicpc.net/problem/5052
"""


class Node:
    def __init__(self):
        self.children = defaultdict(Node)  # 자식 노드들을 저장할 딕셔너리로 초기화
        self.is_end = False  # 해당 노드가 단어의 끝인지 여부를 나타내는 플래그


class Trie:
    def __init__(self):
        self.root = Node()  # 루트 노드 생성

    def insert(self, phone_number):
        node = self.root
        for num in phone_number:
            if num not in node.children:
                node.children[num] = Node()  # 자식 노드 생성
            node = node.children[num]  # 다음 노드로 이동
        node.is_end = True  # 해당 노드가 단어의 끝을 나타내는 플래그 설정

    def check(self, phone_numbers):
        for phone_number in phone_numbers:
            node = self.root
            for num in phone_number:
                if node.is_end:
                    return False  # 다른 번호가 이 번호의 접두사인 경우 False 반환
                node = node.children[num]  # 다음 노드로 이동
        return True  # 모든 번호가 겹치지 않는 경우 True 반환


if __name__ == "__main__":
    input = sys.stdin.readline

    t = int(input())  # 테스트 케이스 수 입력
    for _ in range(t):
        trie = Trie()  # 트라이 객체 생성
        n = int(input())  # 전화번호 개수 입력
        phone_numbers = [input().strip() for _ in range(n)]  # 전화번호들 입력
        for phone_number in phone_numbers:
            trie.insert(phone_number)  # 트라이에 전화번호들 추가

        if trie.check(phone_numbers):
            print("YES")  # 모든 번호가 겹치지 않는 경우
        else:
            print("NO")  # 다른 번호가 접두사인 경우
