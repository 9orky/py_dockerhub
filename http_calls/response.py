from typing import Dict

from pydantic import BaseModel


class HttpCallResponse(BaseModel):
    status_code: int
    json_data: Dict | None = None

    def get_json_value(self, key: str):
        if self.json_data is None:
            return None

        try:
            return self.json_data[key]
        except KeyError:
            return None

    @property
    def is_ok(self) -> bool:
        return 200 <= self.status_code < 300

    @property
    def my_fault(self) -> bool:
        return 400 <= self.status_code < 500

    @property
    def their_fault(self) -> bool:
        return 500 <= self.status_code < 600
