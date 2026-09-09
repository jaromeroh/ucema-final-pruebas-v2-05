import csv
from decimal import Decimal


def get_data(base, scenario):
    if scenario not in {"01", "02", "03"}: raise ValueError("Escenario no autorizado")
    source="datos/ventas_"+scenario+".csv"
    with (base/source).open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    revenue=sum((Decimal(r["revenue"]) for r in rows),Decimal(0))
    previous=sum((Decimal(r["previous_revenue"]) for r in rows),Decimal(0))
    costs=sum((Decimal(r["cost"]) for r in rows),Decimal(0))
    change=float(round((revenue-previous)/previous*100,2)) if previous else None
    losses=[r["region"] for r in rows if Decimal(r["cost"])>Decimal(r["revenue"])]
    return {"scenario":scenario,"source":source,"rows":rows,"revenue_total":float(revenue),
        "margin_total":float(revenue-costs),"change_percent":change,"loss_regions":losses,
        "currency":"USD","scope":"ventas y costo directo; excluye impuestos, devoluciones y gastos generales"}


def validate(output, observation):
    problems=[]
    for field in ["revenue_total","margin_total","change_percent"]:
        actual,expected=output[field],observation[field]
        if expected is None:
            if actual is not None: problems.append(field+": no debe inventar crecimiento sin base")
        elif actual is None or abs(actual-expected)>0.01: problems.append(field+": cálculo incorrecto")
    if observation["loss_regions"] and not output["alerts"]: problems.append("No se informó la pérdida")
    if output["scenario"] != observation["scenario"]: problems.append("Escenario incorrecto")
    if output["requires_human_approval"] is not True: problems.append("Falta aprobación humana")
    return problems
