"""Generated message classes for cloudtrace version v2beta1.

Sends application trace data to Cloud Trace for viewing. Trace data is
collected for all App Engine applications by default. Trace data from other
applications can be provided using this API. This library is used to interact
with the Cloud Trace API directly. If you are looking to instrument your
application for Cloud Trace, we recommend using OpenTelemetry.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'cloudtrace'


class BigQueryOutputConfig(_messages.Message):
  r"""Configuration for the output that is specific to BigQuery when choosing
  a BigQuery dataset as the output destination.

  Enums:
    VariantValueValuesEnum: Optional. Schema variant that should be used when
      exporting data to BigQuery.

  Fields:
    variant: Optional. Schema variant that should be used when exporting data
      to BigQuery.
  """

  class VariantValueValuesEnum(_messages.Enum):
    r"""Optional. Schema variant that should be used when exporting data to
    BigQuery.

    Values:
      SCHEMA_VARIANT_UNSPECIFIED: (Input only) sentinel indicating that the
        API should choose automatically. On create, a value will be selected
        and persisted. Subsequent reads from the API will return a non-default
        value indicating what was selected.
      FIELDS_EXPANDED_AS_COLUMNS: Export data with all attributes and label
        keys of the span expanded as columns dynamically, and each span as a
        row. The attribute/label columns are assigned their associated values
        in that row. We recommend this mode of operation when the number of
        unique label keys are relatively small and stable, as it provides a
        simpler, more convenient query experience.
      CONDENSED_STATIC_JSON: Export data as condensed, json-formatted columns.
        Choose this mode when unique label keys have high cardinality and/or
        change frequently. This schema variant is more scalable and lacks the
        potential issue of reaching the maximum column limit in BigQuery. At
        the same time, this variant is more difficult to query compared with
        `FIELDS_EXPANDED_AS_COLUMNS` mode, often requiring the use of BigQuery
        JSON functions
        (https://cloud.google.com/bigquery/docs/reference/standard-
        sql/json_functions) in order to extract particular labels and use them
        in queries.
    """
    SCHEMA_VARIANT_UNSPECIFIED = 0
    FIELDS_EXPANDED_AS_COLUMNS = 1
    CONDENSED_STATIC_JSON = 2

  variant = _messages.EnumField('VariantValueValuesEnum', 1)


class CloudtraceProjectsTraceSinksCreateRequest(_messages.Message):
  r"""A CloudtraceProjectsTraceSinksCreateRequest object.

  Fields:
    parent: Required. The resource in which to create the sink (currently only
      project sinks are supported): "projects/[PROJECT_ID]" Examples:
      `"projects/my-trace-project"`, `"projects/123456789"`.
    traceSink: A TraceSink resource to be passed as the request body.
  """

  parent = _messages.StringField(1, required=True)
  traceSink = _messages.MessageField('TraceSink', 2)


class CloudtraceProjectsTraceSinksDeleteRequest(_messages.Message):
  r"""A CloudtraceProjectsTraceSinksDeleteRequest object.

  Fields:
    name: Required. The full resource name of the sink to delete, including
      the parent resource and the sink identifier:
      "projects/[PROJECT_NUMBER]/traceSinks/[SINK_ID]" Example:
      `"projects/12345/traceSinks/my-sink-id"`.
  """

  name = _messages.StringField(1, required=True)


class CloudtraceProjectsTraceSinksGetRequest(_messages.Message):
  r"""A CloudtraceProjectsTraceSinksGetRequest object.

  Fields:
    name: Required. The resource name of the sink:
      "projects/[PROJECT_NUMBER]/traceSinks/[SINK_ID]" Example:
      `"projects/12345/traceSinks/my-sink-id"`.
  """

  name = _messages.StringField(1, required=True)


class CloudtraceProjectsTraceSinksListRequest(_messages.Message):
  r"""A CloudtraceProjectsTraceSinksListRequest object.

  Fields:
    pageSize: Optional. The maximum number of results to return from this
      request. Non-positive values are ignored. The presence of
      `next_page_token` in the response indicates that more results might be
      available.
    pageToken: Optional. If present, then retrieve the next batch of results
      from the preceding call to this method. `page_token` must be the value
      of `next_page_token` from the previous response. The values of other
      method parameters should be identical to those in the previous call.
    parent: Required. The parent resource whose sinks are to be listed
      (currently only project parent resources are supported):
      "projects/[PROJECT_ID]"
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class CloudtraceProjectsTraceSinksPatchRequest(_messages.Message):
  r"""A CloudtraceProjectsTraceSinksPatchRequest object.

  Fields:
    name: Required. The full resource name of the sink to update, including
      the parent resource and the sink identifier:
      "projects/[PROJECT_NUMBER]/traceSinks/[SINK_ID]" Example:
      `"projects/12345/traceSinks/my-sink-id"`.
    traceSink: A TraceSink resource to be passed as the request body.
    updateMask: Required. Field mask that specifies the fields in `trace_sink`
      that are to be updated. A sink field is overwritten if, and only if, it
      is in the update mask. `name` and `writer_identity` fields cannot be
      updated. An empty `update_mask` is considered an error. For a detailed
      `FieldMask` definition, see https://developers.google.com/protocol-
      buffers/docs/reference/google.protobuf#fieldmask Example:
      `updateMask=output_config`.
  """

  name = _messages.StringField(1, required=True)
  traceSink = _messages.MessageField('TraceSink', 2)
  updateMask = _messages.StringField(3)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class ListTraceSinksResponse(_messages.Message):
  r"""Result returned from `ListTraceSinks`.

  Fields:
    nextPageToken: A paginated response where more pages might be available
      has `next_page_token` set. To get the next set of results, call the same
      method again using the value of `next_page_token` as `page_token`.
    sinks: A list of sinks.
  """

  nextPageToken = _messages.StringField(1)
  sinks = _messages.MessageField('TraceSink', 2, repeated=True)


class OpenTelemetryFormat(_messages.Message):
  r"""OpenTelemetryFormat contains metadata to help convert Cloud Trace trace
  format to OpenTelemetry trace format.

  Fields:
    version: Optional. OpenTelemetry format defined by
      https://github.com/open-telemetry/opentelemetry-proto/blob/main/opentele
      metry/proto/collector/trace/v1/trace_service.proto Version of the
      OpenTelemetry schema as it appears in the defining proto package.
      Currently, only "v1" is supported, but support for more version may
      added in the future.
  """

  version = _messages.StringField(1)


class OutputConfig(_messages.Message):
  r"""OutputConfig contains a destination for writing trace data.

  Fields:
    bigqueryConfig: Optional. Additional options governing the export behavior
      when the selected destination is a BigQuery dataset.
    destination: Required. The destination for writing trace data. Supported
      formats include:
      "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
    pubsubConfig: Optional. Additional options governing the export behavior
      when the selected destination is a Pub/Sub queue.
  """

  bigqueryConfig = _messages.MessageField('BigQueryOutputConfig', 1)
  destination = _messages.StringField(2)
  pubsubConfig = _messages.MessageField('PubsubOutputConfig', 3)


class PubsubOutputConfig(_messages.Message):
  r"""Configuration for the output that is specific to Pub/Sub when choosing a
  Pub/Sub queue as the output destination.

  Fields:
    openTelemetryFormat: open_telemetry_format contains additional information
      needed to convert Cloud Trace data.
  """

  openTelemetryFormat = _messages.MessageField('OpenTelemetryFormat', 1)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class TraceSink(_messages.Message):
  r"""Describes a sink used to export traces to a BigQuery dataset. The sink
  must be created within a project.

  Fields:
    name: Identifier. The canonical sink resource name, unique within the
      project. Must be of the form:
      projects/[PROJECT_NUMBER]/traceSinks/[SINK_ID]. E.g.:
      `"projects/12345/traceSinks/my-project-trace-sink"`. Sink identifiers
      are limited to 256 characters and can include only the following
      characters: upper and lower-case alphanumeric characters, underscores,
      hyphens, and periods.
    outputConfig: Required. The export destination.
    writerIdentity: Output only. A service account name for exporting the
      data. This field is set by sinks.create and sinks.update. The service
      account will need to be granted write access to the destination
      specified in the output configuration, see [Granting access for a
      resource](/iam/docs/granting-roles-to-service-
      accounts#granting_access_to_a_service_account_for_a_resource). To create
      tables and to write data, this account needs the `dataEditor` role. Read
      more about roles in the [BigQuery
      documentation](https://cloud.google.com/bigquery/docs/access-control).
      E.g.: "service-00000001@00000002.iam.gserviceaccount.com"
  """

  name = _messages.StringField(1)
  outputConfig = _messages.MessageField('OutputConfig', 2)
  writerIdentity = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
