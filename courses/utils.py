from restless.models import serialize

def serialize_page(page, course):
    return serialize(page, include=[
        (
            'course', lambda a: {
            'id': course.id,
            'name': course.name, 
            'description': course.description,
        }),
            ('sections', dict()),
            ('total_pages', lambda a: course.total_pages())
        ])