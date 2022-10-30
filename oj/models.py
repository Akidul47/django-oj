import uuid
from django.db import models
from . import compile

class CompilerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    code = models.TextField()
    success = models.CharField(null=True, blank=True)
    fail = models.CharField(null=True, blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self) -> None:
        cj = compile.CompileJava(code=self.code, id=self.id)
        ret = cj.to_file()
        ret = cj.to_file()
        if not ret:
            print("error writing file: ", ret)
        out, err = cj.compile()
        print("Success: ", out)
        print("Error: ", err)

        self.success = out
        self.fail = err
        return super().save()

    def __str__(self) -> str:
        return str(self.code)