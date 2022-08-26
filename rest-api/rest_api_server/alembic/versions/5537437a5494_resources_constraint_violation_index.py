""""resources_constraint_violation_index"

Revision ID: 5537437a5494
Revises: 2ff7e59fffef
Create Date: 2021-02-26 13:38:31.601265

"""
import os
from pymongo import MongoClient
from config_client.client import Client as EtcdClient

# revision identifiers, used by Alembic.
revision = '5537437a5494'
down_revision = '2ff7e59fffef'
branch_labels = None
depends_on = None
DEFAULT_ETCD_HOST = 'etcd-client'
DEFAULT_ETCD_PORT = 80
INDEX_NAME = 'ResourceConstraintViolated'


def _get_etcd_config_client():
    etcd_host = os.environ.get('HX_ETCD_HOST', DEFAULT_ETCD_HOST)
    etcd_port = os.environ.get('HX_ETCD_PORT', DEFAULT_ETCD_PORT)
    config_cl = EtcdClient(host=etcd_host, port=int(etcd_port))
    return config_cl


def _get_resources_collection():
    config_cl = _get_etcd_config_client()
    mongo_params = config_cl.mongo_params()
    mongo_conn_string = "mongodb://%s:%s@%s:%s" % mongo_params[:-1]
    mongo_client = MongoClient(mongo_conn_string)
    return mongo_client.restapi.resources


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    resources_collection = _get_resources_collection()
    indexes = [x['name'] for x in resources_collection.list_indexes()]
    if INDEX_NAME not in indexes:
        resources_collection.create_index([('constraint_violated', 1)],
                                          name=INDEX_NAME)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    resources_collection = _get_resources_collection()
    indexes = [x['name'] for x in resources_collection.list_indexes()]
    if INDEX_NAME in indexes:
        resources_collection.drop_index(INDEX_NAME)
    # ### end Alembic commands ###