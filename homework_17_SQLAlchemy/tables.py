from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from db_config import get_database_connection_string

connection_string = get_database_connection_string()

engine = create_engine(connection_string)

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class StudentSubject(Base):
    __tablename__ = 'student_subject'
    id = Column(Integer, primary_key = True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    student = relationship("Student")
    subject = relationship("Subject")


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


# student1 = Student(name = 'John', age = 17)
# session.add(student1)

# student2 = Student(name = 'Violetta', age = 18)
# session.add(student2)

# student3 = Student(name = 'Taras', age = 18)
# session.add(student3)

# student4 = Student(name = 'Kateryna', age = 19)
# session.add(student4)

# student5 = Student(name = 'Oleg', age = 17)
# session.add(student5)

# student6 = Student(name = 'Maria', age = 18)
# session.add(student6)

# student7 = Student(name = 'Rachel', age = 19)
# session.add(student7)

# student8 = Student(name = 'Georgiy', age = 20)
# session.add(student8)


# subject1 = Subject(name = 'Math')
# session.add(subject1)

# subject2 = Subject(name = 'Biology')
# session.add(subject2)

# subject3 = Subject(name = 'Science')
# session.add(subject3)

# subject4 = Subject(name = 'English')
# session.add(subject4)

# subject5 = Subject(name = 'Physics')
# session.add(subject5)

# session.commit()

relationships = [
    StudentSubject(student_id=1, subject_id=1),
    StudentSubject(student_id=1, subject_id=2),
    StudentSubject(student_id=2, subject_id=3),
    StudentSubject(student_id=2, subject_id=4),
    StudentSubject(student_id=3, subject_id=1),
    StudentSubject(student_id=3, subject_id=5),
    StudentSubject(student_id=4, subject_id=2),
    StudentSubject(student_id=4, subject_id=3),
    StudentSubject(student_id=5, subject_id=4),
    StudentSubject(student_id=6, subject_id=5),
    StudentSubject(student_id=7, subject_id=1),
    StudentSubject(student_id=8, subject_id=2)
]

# session.add_all(relationships)

english_students = (
    session.query(Student)
    .join(StudentSubject, StudentSubject.student_id == Student.id)
    .join(Subject, Subject.id == StudentSubject.subject_id)
    .filter(Subject.name == 'English')
    .all()
)


for student in english_students:
    print(student.name)



session.commit()
session.close()