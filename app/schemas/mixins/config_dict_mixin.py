from pydantic import BaseModel, ConfigDict

class ConfigDictMixin(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )