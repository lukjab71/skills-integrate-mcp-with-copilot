# Issue drafts to create

This file contains proposed issues based on comparing the project with an existing extracurricular activities management system. Create these issues to track work.

---

## 1) Add persistent database (SQLite) for activities and signups

Description:
- Replace in-memory storage with a persistent database (suggest SQLite for quick setup).
- Create tables: `activities`, `students`, `signups`, `users`.
- Add migrations / SQL schema and sample seed data.
- Update `/activities`, `/activities/{name}/signup` and `/activities/{name}/unregister` to use DB.

Acceptance criteria:
- Data persists after server restart; endpoints return same JSON shape.

Labels: enhancement, backend

---

## 2) Admin panel and CRUD endpoints for students & activities

Description:
- Add admin-only endpoints to Create / Read / Update / Delete students and activities.
- Endpoints examples: `GET/POST/PUT/DELETE /admin/activities`, `GET/POST/PUT/DELETE /admin/students`.
- Provide a minimal admin static page or document example API usage.

Acceptance criteria:
- Admin can add/edit activity metadata (description, schedule, max_participants) and manage student profiles.

Labels: feature, admin

---

## 3) Implement authentication and roles (admin vs student)

Description:
- Add simple auth: admin registration, login, and role-based access control.
- Suggest JWT-based tokens or FastAPI sessions; store user records securely with hashed passwords.
- Protect admin endpoints so only admins can access them.

Acceptance criteria:
- Admin endpoints require authentication; student signup endpoints remain public or optionally require login.

Labels: security, feature

---

## 4) Add profile photos and student profile support (file upload)

Description:
- Add file upload for student profile photos.
- Store files on disk (recommended) and save paths in DB; validate types and size.
- Update student model and admin UI to upload/change photos.

Acceptance criteria:
- Successful upload, served from `/static` or protected route; images not stored as raw blobs in DB.

Labels: feature, ui

---

## 5) Improve security: input validation, prepared statements, and secrets handling

Description:
- Replace any string-built SQL with parameterized queries (use SQLAlchemy or `databases`).
- Ensure passwords use `bcrypt`/`password_hash`.
- Add basic input validation and error handling.
- Move credentials out of repo into env/config and add `.env` example.

Acceptance criteria:
- No raw SQL string concatenation in code; secrets not hard-coded.

Labels: security, cleanup

---

## 6) Add tests and CI for basic endpoints

Description:
- Add minimal unit/integration tests for GET `/activities`, signup and unregister flows.
- Add GitHub Actions workflow to run tests on push.

Acceptance criteria:
- Tests run in CI and pass for basic flows.

Labels: tests, ci
