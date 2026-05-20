class RankingBoard:
    def __init__(self):
        self.records = []
    
    def add_record(self, nickname, life):
        record = {
            "name": nickname,
            "life": life
        }

        self.records.append(record)

    def show_ranking(self):
        if len(self.records) == 0:
            print("등록된 기록이 없습니다.")
            return

        self.records.sort(key=lambda x: (-x["life"], x["name"]))

        print("----레코드----")

        for i in range(min(3, len(self.records))):
            print(f"{i + 1}위 {self.records[i]['name']} {self.records[i]['life']}회")
