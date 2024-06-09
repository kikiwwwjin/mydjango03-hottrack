from django.db import models
from datetime import datetime, timedelta

# 쿼리셋
class FinalMdQuerySet(models.QuerySet):

    # 자동 매일 정제된 결과
    def daily_refined(self):
        # 오늘 생성된 해시코드(어제 수집된 해시코드) 추출
        # 하루전
        today_date = datetime.today()
        yesterday_date = today_date - timedelta(days=1)
        yes_date = yesterday_date.strftime('%Y-%m-%d')
        return self.filter(reg_date=yes_date)

    # 매일 MD에 반영 확정된 결과
    # def daily_fixed(self):
    #     return self.filter()


class MassFinalMdDataPo(models.Model):
    hashcode = models.CharField(primary_key=True, max_length=64)
    title = models.TextField(blank=True, null=True)
    option_name = models.TextField(blank=True, null=True)
    search_keyword = models.TextField(blank=True, null=True)
    result_target = models.TextField(blank=True, null=True)
    bon_malls = models.TextField(blank=True, null=True)
    mall_pid = models.TextField(blank=True, null=True)
    fixed_ctime = models.TextField(blank=True, null=True)
    reg_date = models.TextField(blank=True, null=True)
    reg_time = models.TextField(blank=True, null=True)
    oper_serialno = models.TextField(blank=True, null=True)
    refine_code = models.TextField(blank=True, null=True)
    deleted_keywords = models.TextField(blank=True, null=True)
    abs_model = models.TextField(blank=True, null=True)

    # 쿼리셋 변경 적용
    objects = FinalMdQuerySet.as_manager()


    class Meta:
        managed = True
        db_table = 'mass_final_md_data_po'








#
#
#
# # Create your models here.
# # 정제 결과 가져오는 Class
# class FinalMd(models.Model):
#     # 필드정의
#     hashcode = models.CharField(max_length=64)
#     title = models.CharField(max_length=512)
#     option_name = models.CharField(max_length=512)
#     search_keyword = models.CharField(max_length=100)
#     result_target = models.CharField(max_length=2058)
#     bon_malls = models.CharField(max_length=64)
#     mall_pid = models.CharField(max_length=128)
#     fixed_ctime = models.CharField(max_length=128)
#     reg_date = models.DateField()
#     reg_time = models.DateTimeField()
#     oper_serialno = models.CharField(max_length=64)
#     refine_code = models.IntegerField(max_length=2)
#     deleted_keywords = models.CharField(max_length=2058)
#     abs_model = models.CharField(max_length=2058)
#
#     # 쿼리셋 변경 적용
#     objects = FinalMdQuerySet.as_manager()
#
#     # 테이블명 강제 지정
#     class Meta:
#         db_table = 'mass_final_md_data_po'




