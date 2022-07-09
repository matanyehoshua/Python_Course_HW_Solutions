# RepoDB Class:

class RepoDb:
    def __init__(self, local_session):
        self.local_session = local_session

    def get_by_id(self, table_class, id):
        return self.local_session.query(table_class).get(id)

    def get_all(self, table_class):
        return self.local_session.query(table_class).all()

    def reset_auto_inc(self, table_class):
        self.local_session.execute(f'TRUNCATE TABLE {table_class.__tablename__} RESTART IDENTITY CASCADE')

    def add(self, one_row):
        self.local_session.add(one_row)
        self.local_session.commit()
