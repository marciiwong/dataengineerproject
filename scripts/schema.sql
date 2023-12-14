DO $$ 
BEGIN
    IF EXISTS (SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'raw') THEN
        DROP SCHEMA raw CASCADE;
    END IF;
    CREATE SCHEMA raw;
END $$;
