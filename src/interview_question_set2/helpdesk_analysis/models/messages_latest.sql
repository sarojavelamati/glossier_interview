{{ config(
    materialized='incremental',
    unique_key='message_id'
) }}

WITH latest_messages AS (
    SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY message_id ORDER BY synced_at DESC) AS row_num
    FROM
        {{ ref('messages') }}
)

SELECT
    id,
    ticket_id,
    message_id,
    customer_id,
    agent_id,
    direction,
    created_at,
    synced_at
FROM
    latest_messages
WHERE
    row_num = 1

{% if is_incremental() %}
    AND synced_at > (SELECT MAX(synced_at) FROM {{ this }})
{% endif %}
