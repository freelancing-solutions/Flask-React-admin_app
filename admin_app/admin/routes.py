from flask import Blueprint, render_template, url_for, request
from admin_app.main import api_fetcher, api_sender
admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/', methods=["GET"])
def home() -> tuple:
    return render_template('index.html')


@admin_bp.route('/data/<path:path>', methods=["GET", "POST"])
def data(path: str) -> tuple:
    
    if request.method == "GET":
        if path == "exchange":
            return render_template("forms/exchange.html")
        elif path == "broker":
            return render_template("forms/broker.html")
        elif path == "stock":
            return render_template("forms/stock.html")
    else:
        json_data: dict = request.get_json()
        if path == "exchange":
            return api_sender.send_exchange(exchange=json_data)
        elif path == "broker":
            return api_sender.send_broker(broker=json_data)
        elif path == "stock":
            return api_sender.send_stock(stock=json_data)


@admin_bp.route('/data/<path:resource>/edit/<path:uid>', methods=["GET", "POST"])
def data_edit(resource: str, uid: str) -> tuple:

    if request.method == "GET":
        if resource == "exchange":
            response = api_fetcher.fetch_exchange(exchange_id=uid)
            response_code: int = int(response[1])
            if response_code == 200:
                exchange_data: dict = response[0].get_json().get('payload')
                return render_template("forms/edit-exchange.html", exchange_data=exchange_data)
            else:
                # let error handlers handle this problem
                pass
        elif resource == "broker":
            response = api_fetcher.fetch_broker(broker_id=uid)
            response_code: int = int(response[1])
            if response_code == 200:
                broker_data: dict = response[0].get_json().get('payload')
                return render_template("forms/edit-broker.html", broker_data=broker_data)
        elif resource == "stock":
            response = api_fetcher.fetch_stock(stock_id=uid)
            response_code: int = int(response[1])
            if response_code == 200:
                stock_data: dict = response[0].get_json().get('payload')
                return render_template("forms/edit-stock.html", stock_data=stock_data)
    else:
        json_data: dict = request.get_json()
        if resource == "exchange":
            return api_sender.send_exchange(exchange=json_data)
        elif resource == "broker":
            return api_sender.send_broker(broker=json_data)
        elif resource == "stock":
            return api_sender.send_stock(stock=json_data)


@admin_bp.route('/settings/<path:path>', methods=["GET", "POST"])
def settings(path):
    if path == "api":
        return render_template("api/settings.html")
    elif path == "scrapper":
        return render_template("scrapper/settings.html")


@admin_bp.route('/schedules/<path:path>', methods=["GET", "POST"])
def schedules(path):
    if path == "api":
        return render_template("api/schedules.html")
    elif path == "scrapper":
        return render_template("scrapper/schedules.html")


@admin_bp.route('/logs/<path:path>', methods=["GET"])
def logs(path):
    if path == "api":
        return render_template("api/logs.html")
    elif path == "scrapper":
        return render_template("scrapper/logs.html")

