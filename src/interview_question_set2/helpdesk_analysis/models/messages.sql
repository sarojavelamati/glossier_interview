{{ config(
    materialized='table'
) }}

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
    main.messages  -- Explicitly specify the schema as "main"
