{{ config(
    materialized='table'
) }}

WITH ticket_data AS (
    SELECT
        t.ticket_id,
        t.subject,
        t.customer_id,
        t.agent_id,
        t.tags,
        t.created_at AS ticket_created_at,
        t.synced_at AS ticket_synced_at
    FROM
        {{ ref('tickets_latest') }} AS t
),

message_counts AS (
    SELECT
        m.ticket_id,
        COUNT(CASE WHEN direction = 'in' THEN 1 END) AS inbound_messages,
        COUNT(CASE WHEN direction = 'out' THEN 1 END) AS outbound_messages
    FROM
        {{ ref('messages_latest') }} AS m
    GROUP BY
        m.ticket_id
)

SELECT
    td.*,
    mc.inbound_messages,
    mc.outbound_messages
FROM
    ticket_data AS td
LEFT JOIN
    message_counts AS mc ON td.ticket_id = mc.ticket_id