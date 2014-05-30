METAEXTRACTOR_CONFIG = { } #default configuration

#METAEXTRACTOR_CONFIG = { 'plugins' : ['htmlfetch','schematoplugin'] }
#METAEXTRACTOR_CONFIG['field_priority'] = { 'link' : [ 'schematoplugin', 'htmlfetch' ] }



# *** schemato configuration ***********
VALIDATOR_MODULES = [
    "schemas.rnews.RNewsValidator",
    "schemas.opengraph.OpenGraphValidator",
    "schemas.schemaorg.SchemaOrgValidator",
    "schemas.schemaorg_rdf.SchemaOrgRDFaValidator",
    "schemas.parselypage.ParselyPageValidator",
]

# root of schema cache
CACHE_ROOT = "/tmp"
# how many seconds to wait until re-cache
CACHE_EXPIRY = 60 * 60 * 500

# *** end schemato configuration *******