# hashtable/structures.py

class MyHashTable:
    def __init__(self, size=100):
        """
        해시 테이블 초기화.
        :param size: 해시 테이블의 크기(기본값은 100).
        """
        self.size = size
        self.hashmap = [[] for _ in range(size)]  # 각 슬롯은 (key, value) 쌍의 리스트로 구성됩니다.

    def _hash_function(self, key):
        """
        해시 함수: 키를 해시 테이블의 인덱스로 변환.
        :param key: 해시 테이블에 저장할 키.
        :return: 해시 테이블의 인덱스.
        """
        return hash(key) % self.size

    def put(self, key, value):
        """
        해시 테이블에 키-값 쌍을 삽입합니다.
        :param key: 삽입할 키.
        :param value: 삽입할 값.
        :slot: 해당 인덱스에 위치한 리스트(해시 버킷)
        """
        index = self._hash_function(key)
        slot = self.hashmap[index] # 해당 인덱스의 슬롯(리스트)을 가져옵니다.

        
        for i, (k, v) in enumerate(slot):
            if k == key:
                slot[i] = (key, value)  # 이미 존재하는 키가 있는 경우는 업데이트를 통해 기존 값을 덮어씌움
                return
            
        #  체이닝(Chaining)
        slot.append((key, value))  # 새로 추가된 키-값 튜플은 항상 연결 리스트의 끝에 추가됨

    def get(self, key):
        """
        주어진 키에 해당하는 값을 반환합니다.
        :param key: 검색할 키.
        :return: 키에 해당하는 값 또는 -1 (키가 존재하지 않는 경우).
        """
        index = self._hash_function(key)
        slot = self.hashmap[index]

        for k, v in slot:
            if k == key:
                return v  # 키에 해당하는 값을 반환합니다.

        return -1  # 키가 존재하지 않으면 -1을 반환합니다.

    def remove(self, key):
        """
        주어진 키에 해당하는 키-값 쌍을 삭제합니다.
        :param key: 삭제할 키.
        """
        index = self._hash_function(key)
        slot = self.hashmap[index]

        for i, (k, v) in enumerate(slot):
            if k == key:
                del slot[i]  # 키-값 쌍을 삭제합니다.
                return

    def display(self):
        """
        해시 테이블의 현재 상태를 출력합니다.
        """
        for index, slot in enumerate(self.hashmap):
            print(f"Index {index}: {slot}")