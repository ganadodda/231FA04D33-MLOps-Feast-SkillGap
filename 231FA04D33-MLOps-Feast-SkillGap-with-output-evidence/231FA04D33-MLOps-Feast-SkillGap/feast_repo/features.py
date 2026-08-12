from datetime import timedelta
from feast import Entity, FeatureView, FeatureService, Field, FileSource
from feast.types import Float32, Int64

student = Entity(name="student", join_keys=["student_id"], description="CSE student")

cse_skill_source = FileSource(
    name="cse_skill_source",
    path="data/cse_skill_features.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp"
)

cse_skill_feature_view = FeatureView(
    name="cse_skill_features",
    entities=[student],
    ttl=timedelta(days=3650),
    schema=[
        Field(name="Programming", dtype=Int64),
        Field(name="Database", dtype=Int64),
        Field(name="Problem_Solving", dtype=Int64),
        Field(name="Communication", dtype=Int64),
        Field(name="Cloud_Computing", dtype=Int64),
        Field(name="Data_Analysis", dtype=Int64),
        Field(name="Teamwork", dtype=Int64),
        Field(name="Aptitude", dtype=Int64),
        Field(name="technical_skill_score", dtype=Float32),
        Field(name="professional_skill_score", dtype=Float32),
        Field(name="calculated_skill_score", dtype=Float32),
    ],
    source=cse_skill_source,
    online=True
)

cse_skill_feature_service = FeatureService(
    name="cse_skill_gap_service",
    features=[cse_skill_feature_view]
)
