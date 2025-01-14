# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

from puzzle.ext import db

BP_NAME = __name__.split('.')[-2]
blueprint = Blueprint(BP_NAME, __name__, template_folder='templates',
                      static_folder='static',
                      static_url_path="/{}/static".format(BP_NAME))


@blueprint.route('/')
def index():
    """Show the landing page."""
    return render_template('index.html', vcf_files=db.vcf_files())
