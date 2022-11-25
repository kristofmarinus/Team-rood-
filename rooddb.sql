BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "projects" (
	"pk_project_id"	INTEGER NOT NULL,
	"project_name"	TEXT NOT NULL,
	"project_descr"	TEXT NOT NULL,
	"fk_customer_id"	INTEGER NOT NULL,
	"project_date_added"	TEXT NOT NULL,
	"project_deadline"	TEXT NOT NULL,
	"project_finished"	TEXT,
	"Field8"	INTEGER
);
CREATE TABLE IF NOT EXISTS "tasks" (
	"pk_task_id"	INTEGER NOT NULL,
	"task_descr"	TEXT NOT NULL,
	"fk_project_id"	INTEGER NOT NULL,
	"fk_user_id"	INTEGER NOT NULL,
	"task_date_added"	TEXT,
	"task_deadline"	TEXT,
	"task_progress"	INTEGER,
	"task_started_on"	TEXT,
	"task_finished_on"	TEXT,
	PRIMARY KEY("pk_task_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "users" (
	"pk_user_id"	INTEGER NOT NULL,
	"user_name"	TEXT NOT NULL,
	PRIMARY KEY("pk_user_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "customers" (
	"pk_customer_id"	INTEGER NOT NULL,
	"customer_first_name"	TEXT NOT NULL,
	"customer_last_name"	TEXT NOT NULL,
	"customer_website"	TEXT,
	"customer_email_address"	TEXT NOT NULL,
	PRIMARY KEY("pk_customer_id" AUTOINCREMENT)
);
COMMIT;
