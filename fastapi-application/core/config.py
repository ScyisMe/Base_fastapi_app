from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn
from pydantic import BaseModel

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    
class ApiPrefix(BaseModel):
    prefix: str = "/api"
    
class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    
    name_convention: dict[str, str] =  {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
    }


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env",".env.template"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()    
    db: DatabaseConfig 


setting = Setting()
print(setting.db.url)
print(setting.db.echo)