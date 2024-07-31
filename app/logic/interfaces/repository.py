from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.colliving import House, Resident, Room, User


class HouseRepository(ABC):
    @abstractmethod
    async def add(self, home: House) -> House: ...

    @abstractmethod
    async def get_by_uuid(self, uuid: str) -> Optional[House]: ...


class UserRepository(ABC):
    @abstractmethod
    async def add(self, user: User) -> User: ...

    @abstractmethod
    async def get_by_uuid(self, uuid: str) -> Optional[User]: ...


class RoomRepository(ABC):
    @abstractmethod
    async def add(self, room: Room) -> Room: ...

    @abstractmethod
    async def get_by_uuid(self, uuid: str) -> Optional[Room]: ...


class ResidentRepository(ABC):
    @abstractmethod
    async def add(self, resident: Resident) -> Resident: ...

    @abstractmethod
    async def get_by_uuid(self, uuid: str) -> Optional[Resident]: ...

    @abstractmethod
    async def get_by_room_uuid(self, room_uuid: str) -> list[Resident]: ...
