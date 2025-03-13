from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association table for the many-to-many relationship between Advocate and Case
advocate_case_association = Table(
    'advocate_case', Base.metadata,
    Column('advocate_id', Integer, ForeignKey('advocate.id'), primary_key=True),
    Column('case_id', Integer, ForeignKey('case.id'), primary_key=True)
)

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    cases = relationship('Case', back_populates='client')

class Case(Base):
    __tablename__ = 'case'
    id = Column(Integer, primary_key=True)
    case_name = Column(String, nullable=False)
    case_description = Column(String)
    status = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship('Client', back_populates='cases')
    court_date = Column(Date)
    event_type = Column(String)
    court_name = Column(String)
    judge_name = Column(String)
    advocates = relationship('Advocate', secondary=advocate_case_association, back_populates='cases')
    case_details = relationship('CaseDetails', uselist=False, back_populates='case')
    documents = relationship('Document', back_populates='case')

class CaseDetails(Base):
    __tablename__ = 'case_details'
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey('case.id'), unique=True)
    Summary = Column(String, nullable= False)
    agreed_fee = Column(Integer)
    case = relationship('Case', back_populates='case_details')

class Document(Base):
    __tablename__ = 'document'
    document_id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey('case.id'))
    file_path = Column(String, nullable=False)
    description = Column(String)
    case = relationship('Case', back_populates='documents')

class Advocate(Base):
    __tablename__ = 'advocate'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    cases = relationship('Case', secondary=advocate_case_association, back_populates='advocates')
