from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
import io
import csv
from objects.soldier import Soldier
from objects.room import Room
from objects.dorm import Dorm
from  objects.base import Base


app = FastAPI()


@app.post("/assignWithCsv")
def assign_from_csv(file: UploadFile):
    if file.content_type != "text/csv":
        return {"error": "file must be a csv"}

    content = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    soldiers_data_list = list(reader)
    sorted_list = sorted(soldiers_data_list, key=lambda x: int(x[5]), reverse=True)

    base = Base()
    dorm_a = base.dormA
    dorm_b = base.dormB


    for line in sorted_list:
        soldier = Soldier(int(line[0]), line[1], line[2], line[3], line[4], int(line[5]), True)
        base.waiting_list.append(soldier)
    for room in dorm_a.rooms:
        for _ in range(8):
            if base.waiting_list:
                room.assign_to_room(base.waiting_list.pop(0))


    for room in dorm_b.rooms:
        for _ in range(8):
            if base.waiting_list:
                room.assign_to_room(base.waiting_list.pop(0))

    for soldier in base.waiting_list and base.waiting_list:
        soldier.is_assigned = False

    # state = []
    # for soldier in sorted_list:
    #     if soldier.is_assigned:
    #         state.append({"name": soldier[0] + " " + soldier[1]})
    #     else:
    #         state.append({"name": soldier[0] + " " + soldier[1], "is waiting": "yes"})


    return {"number of soldiers signed": len(sorted_list) - len(base.waiting_list), "waiting": len(base.waiting_list)}


