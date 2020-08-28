from flask import Flask


def create_api(config):

    from api.basemodels import db
    from api.baseviews import generate_password_hash
    from api.baseviews import login_required
    # from api.telegram.bot import TelegramBot
    # from api.telegram.client import TelegramClient
    from flask import send_from_directory
    from flask import render_template
    from os.path import join

    api = Flask(__name__, template_folder='../client/public',
                static_folder='../client/static')

    api.config.from_object(config)
    db.init_app(api)

    #bot = TelegramBot(config.TELEGRAM_BOT_TOKEN)
    #bot.start()

    # client = TelegramClient(config.TELEGRAM_API_ID,
    #                         config.TELEGRAM_API_HASH)
    #client.start()

    @api.route('/')
    def index():
        return render_template('index.html')

    from api.baseviews import signin
    api.register_blueprint(signin, url_prefix='/api/v1/')

    return api
