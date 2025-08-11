--task-1
--Yangi database yaratish va Roster jadvalini Name (TEXT), Species (TEXT), Age (INTEGER) ustunlari bilan yaratish.
CREATE DATABASE StarTrekDB;

\c startrekdb;  -- Bu qator faqat PostgreSQL uchun, MySQL'da USE StarTrekDB;

CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);

--task-2
--Jadvalni berilgan ma’lumotlar bilan to‘ldirish.
INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);

--task-3
--Jadzia Dax ismini Ezri Dax ga yangilash.
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';

--task-4
--Species ustuni Bajoran bo‘lganlarning Name va Age ustunlarini chiqarish.
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran';
