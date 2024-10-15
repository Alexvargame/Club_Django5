from estate.models.comments import Comment

class CommentRepository:
    model = Comment

    def create_object(self, dto):

        comment = self.model.objects.create(
            real_state=dto.real_state,
            author=dto.author,
            content=dto.content,
        )
        comment.save()

    def list_objects(self, rs=None):
        if rs:
          return self.model.objects.filter(real_state=rs.pk)
        return self.model.objects.all()