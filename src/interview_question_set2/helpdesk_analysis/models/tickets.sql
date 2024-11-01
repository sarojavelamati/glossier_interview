{{ config(
    materialized='table'
) }}

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
    {{ source('helpdesk', 'tickets') }}
