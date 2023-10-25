from ninja import Router


router = Router()


@router.get("status/all", response=list)
def all_status(request):
    return ["Pending", "In Progress", "Complete"]


@router.get("type/all", response=list)
def all_type(request):
    return ["Unclassified", "Classified", "Secret", "Top Secret"]