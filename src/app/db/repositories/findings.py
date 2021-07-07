from app.db.repositories.base import BaseRepository
from app.models.finding import FindingBase, FindingInDB


CREATE_FINDING_QUERY = """
    INSERT INTO finding (finding_class_id, application_id, uri, signature, state, create_time, update_time)
    VALUES (:finding_class_id, :application_id, :uri, :signature, :state, :create_time, :update_time)
    RETURNING id, finding_class_id, state;
"""

class FindingsRepository(BaseRepository):
    """"
    All database actions associated with the Finding resource
    """

    async def create_finding(self, *, new_finding: FindingBase) -> FindingInDB:
        query_values = new_finding
        finding = await self.db.fetch_one(query=CREATE_FINDING_QUERY, values=query_values)

        return FindingInDB(**finding)
