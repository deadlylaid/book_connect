from django.conf import settings
from haystack.backends.elasticsearch_backend import ElasticsearchSearchBackend
from haystack.backends.elasticsearch_backend import ElasticsearchSearchEngine
from haystack.constants import DEFAULT_OPERATOR, DJANGO_CT, DJANGO_ID, FUZZY_MAX_EXPANSIONS, FUZZY_MIN_SIM, ID

# Elasticsearch + mecab-ko Configurate


# Haystack's Elasticsearch Backend Configure
class ConfigurableElasticBackend(ElasticsearchSearchBackend):
    pass


# Haystack's Elasticsearch Engine Configure
class ConfigurableElasticSearchEngine(ElasticsearchSearchEngine):
    backend = ConfigurableElasticBackend
