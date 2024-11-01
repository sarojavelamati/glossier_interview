{{ config(
    materialized='incremental',
    unique_key='ticket_id'
) }}

WITH latest_tickets AS (
    SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY ticket_id ORDER BY synced_at DESC) AS row_num
    FROM
        {{ ref('tickets') }}
)

SELECT
    id,
    ticket_id,
    subject,
    customer_id,
    agent_id,
    tags,
    created_at,
    synced_at
FROM
    latest_tickets
WHERE
    row_num = 1

{% if is_incremental() %}
    AND synced_at > (SELECT MAX(synced_at) FROM {{ this }})
{% endif %}
