from . import db

# https://dormousehole.readthedocs.io/en/latest/patterns/sqlalchemy.html
# 增删改查 https://blog.csdn.net/Co_zy/article/details/77937195

class IpCount(db.Model):
    __tablename__ = 'ipcount'
    id = db.Column(db.Integer, primary_key = True)
    ip = db.Column(db.String(256), index = True, unique = True)
    count = db.Column(db.Integer, index = True, default=0)

    def __init__(self, ip=None, count=None):
        self.ip = ip
        self.count = count

    @classmethod
    def get_count(cls, ip):
        count = cls.query.filter(IpCount.ip==ip).first()
        if None == count:
            return 0            
        
        return count.count
    
    @classmethod
    def set_count(cls, ip, count):
        
        ipCount = cls.query.filter(IpCount.ip==ip).first()
        if None == ipCount:
            ipCount = IpCount(ip, count)
            db.session.add(ipCount)
            db.session.commit()
        
        ipCount.count = count
        db.session.commit()