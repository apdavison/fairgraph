name_or_id_in_ = {
  "@context": {
    "fieldname": {
      "@type": "@id",
      "@id": "fieldname"
    },
    "@vocab": "https://schema.hbp.eu/graphQuery/",
    "merge": {
      "@type": "@id",
      "@id": "merge"
    },
    "relative_path": {
      "@type": "@id",
      "@id": "relative_path"
    }
  },
  "fields": [
    {
      "fieldname": "query:activity",
      "relative_path": "https://schema.hbp.eu/minds/activity"
    },
    {
      "fieldname": "query:component",
      "relative_path": "https://schema.hbp.eu/minds/component"
    },
    {
      "fieldname": "query:contributors",
      "relative_path": "https://schema.hbp.eu/minds/contributors"
    },
    {
      "fieldname": "query:createdAt",
      "relative_path": "https://schema.hbp.eu/provenance/createdAt"
    },
    {
      "fieldname": "query:created_at",
      "relative_path": "https://schema.hbp.eu/minds/created_at"
    },
    {
      "fieldname": "query:datalink",
      "relative_path": "http://schema.org/datalink"
    },
    {
      "fieldname": "query:datalink",
      "relative_path": "https://schema.hbp.eu/minds/datalink"
    },
    {
      "fieldname": "query:embargo_status",
      "relative_path": "https://schema.hbp.eu/minds/embargo_status"
    },
    {
      "fieldname": "query:formats",
      "relative_path": "https://schema.hbp.eu/minds/formats"
    },
    {
      "fieldname": "query:license",
      "relative_path": "https://schema.hbp.eu/minds/license"
    },
    {
      "fieldname": "query:owners",
      "relative_path": "https://schema.hbp.eu/minds/owners"
    },
    {
      "fieldname": "query:publications",
      "relative_path": "https://schema.hbp.eu/minds/publications"
    },
    {
      "fieldname": "query:release_date",
      "relative_path": "https://schema.hbp.eu/minds/release_date"
    },
    {
      "fieldname": "query:specimen_group",
      "relative_path": "https://schema.hbp.eu/minds/specimen_group"
    },
    {
      "fieldname": "query:description",
      "relative_path": "http://schema.org/description"
    },
    {
      "fieldname": "query:name",
      "relative_path": "http://schema.org/name",
      "filter": {
        "op": "contains",
        "parameter": "name"
      }
    },
    {
      "fieldname": "query:identifier",
      "relative_path": "http://schema.org/identifier"
    },
    {
      "fieldname": "query:qualifiedAssociation",
      "relative_path": "http://www.w3.org/ns/prov#qualifiedAssociation"
    },
    {
      "fieldname": "query:@id",
      "relative_path": "@id",
      "filter": {
        "op": "contains",
        "parameter": "id"
      }
    },
    {
      "fieldname": "query:datasetDOI",
      "relative_path": "https://schema.hbp.eu/minds/datasetDOI"
    },
    {
      "fieldname": "query:container_url",
      "relative_path": "https://schema.hbp.eu/minds/container_url"
    },
    {
      "fieldname": "query:license_info",
      "relative_path": "https://schema.hbp.eu/minds/license_info"
    },
    {
      "fieldname": "query:parcellationRegion",
      "relative_path": "https://schema.hbp.eu/minds/parcellationRegion"
    },
    {
      "fieldname": "query:reference_space",
      "relative_path": "https://schema.hbp.eu/minds/reference_space"
    }
  ]
}
