from DB.models import Size


class SizeCreator:
    def create(self):
        size = [
            Size(name="XS"),
            Size(name="XL"),
            Size(name="XXl"),
            Size(name="S"),
            Size(name="M"),
            Size(name="MX"),
            Size(name="LS"),
            Size(name="TG"),
            Size(name="PG"),
            Size(name="LK"),
            Size(name="KS"),
            Size(name="CG"),
            Size(name="L"),
            Size(name="GG"),
            Size(name="140/40"),
            Size(name="260/100"),
            Size(name="10/100"),
            Size(name="50/70"),
            Size(name="60/90"),
            Size(name="74*70"),
        ]
        Size.objects.bulk_create(size)
        return size
