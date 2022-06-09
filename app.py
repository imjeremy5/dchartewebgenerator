from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = "doodoocacapoop6969"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/transport", methods=["POST", "GET]"])
def transport():
    return render_template("transport.html")


@app.route("/refusal", methods=["POST", "GET]"])
def refusal():
    return render_template("refusal.html")


@app.route("/tgenerator", methods=["POST", "GET]"])
def tgenerator():
    unit = str(request.form['unit'])
    address = str(request.form['address'])
    city = str(request.form['city'])
    rfd = str(request.form['rfd'])
    age = str(request.form['age'])
    au = str(request.form['au'])
    sex = str(request.form['sex'])
    pf = str(request.form['pf'])
    cc = str(request.form['cc'])
    hpi = str(request.form['hpi'])
    ls = str(request.form['ls'])
    loc = str(request.form['loc'])
    ps = str(request.form['ps'])
    pc = str(request.form['pc'])
    mon = str(request.form['mon'])
    rhythm = str(request.form['rhythm'])
    ass_text = str(request.form['ass_text'])
    changes_text = str(request.form['changes_text'])
    treatment_text = str(request.form['treatment_text'])
    name = str(request.form['name'])
    rn = str(request.form['rn'])
    time = str(request.form['time'])
    exceptions_text = str(request.form['exceptions_text'])

    if changes_text == "":
        if exceptions_text == "":
            if mon == "5 lead":
                flash("Dispatch:", "h1")
                flash("{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format( unit, address, city, rfd, age, au, sex, pf), "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash("Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with no significant change.".format(loc, ls, pc, ps, ass_text, mon, rhythm,), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash("Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format( name, rn, time), "transport")
                flash(name, "sig")
            elif mon == "12 lead":
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city, rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, ), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash(name, "sig")
            else:
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city, rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patients vitals, condition, and lung sounds monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text,), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash(name, "sig")
        else:
            if mon == "5 lead":
                flash("Dispatch:", "h1")
                flash("{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city,
                                                                                                        rfd, age, au, sex,
                                                                                                        pf), "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, ), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
            elif mon == "12 lead":
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city,
                                                                                                      rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, ), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
            else:
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city,
                                                                                                      rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patients vitals, condition, and lung sounds monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text,), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
    else:
        if exceptions_text == "":
            if mon == "5 lead":
                flash("Dispatch:", "h1")
                flash("{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format( unit, address, city, rfd, age, au, sex, pf), "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash("Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with {}".format(loc, ls, pc, ps, ass_text, mon, rhythm, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash("Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format( name, rn, time), "transport")
                flash(name, "sig")
            elif mon == "12 lead":
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city, rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with {}".format(loc, ls, pc, ps, ass_text, mon, rhythm, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash(name, "sig")
            else:
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city, rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patients vitals, condition, and lung sounds monitored throughout care, before and after all inteventions with {}".format(
                        loc, ls, pc, ps, ass_text, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash(name, "sig")
        else:
            if mon == "5 lead":
                flash("Dispatch:", "h1")
                flash("{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city,
                                                                                                        rfd, age, au, sex,
                                                                                                        pf), "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with {}".format(loc, ls, pc, ps, ass_text, mon, rhythm, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
            elif mon == "12 lead":
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city,
                                                                                                      rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with {}".format(loc, ls, pc, ps, ass_text, mon, rhythm, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
            else:
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address, city,
                                                                                                      rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patients vitals, condition, and lung sounds monitored throughout care, before and after all inteventions with {}.".format(
                        loc, ls, pc, ps, ass_text, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "Patient stated they wanted to be transported to KRMC by ambulance. Loaded patient onto gurney and into ambulance for transport with {}. Patch was made to KRMC ER with no questions or orders. Patient was stable upon transfer of care to {} at {}.".format(
                        name, rn, time), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")

    return render_template("tgenerator.html")

@app.route("/rgenerator", methods=["POST", "GET]"])
def rgenerator():
    unit = str(request.form['unit'])
    address = str(request.form['address'])
    city = str(request.form['city'])
    rfd = str(request.form['rfd'])
    age = str(request.form['age'])
    au = str(request.form['au'])
    sex = str(request.form['sex'])
    pf = str(request.form['pf'])
    cc = str(request.form['cc'])
    hpi = str(request.form['hpi'])
    ls = str(request.form['ls'])
    loc = str(request.form['loc'])
    ps = str(request.form['ps'])
    pc = str(request.form['pc'])
    mon = str(request.form['mon'])
    rhythm = str(request.form['rhythm'])
    ass_text = str(request.form['ass_text'])
    changes_text = str(request.form['changes_text'])
    treatment_text = str(request.form['treatment_text'])
    name = str(request.form['name'])
    exceptions_text = str(request.form['exceptions_text'])
    rof = str(request.form['rof'])
    callback = str(request.form['callback'])
    sign_refusal = str(request.form['sign_refusal'])

    if changes_text == "":
        if exceptions_text == "":
            if mon == "5 lead":
                flash("Dispatch:", "h1")
                flash("{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                        city, rfd, age,
                                                                                                        au, sex, pf),
                      "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, ), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash(name, "sig")
            elif mon == "12 lead":
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                      city, rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, ), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash(name, "sig")
            else:
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                      city, rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patients vitals, condition, and lung sounds monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text, ), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash("The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash(name, "sig")
        else:
            if mon == "5 lead":
                flash("Dispatch:", "h1")
                flash("{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                        city,
                                                                                                        rfd, age, au,
                                                                                                        sex,
                                                                                                        pf), "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, ), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
            elif mon == "12 lead":
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                      city,
                                                                                                      rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, ), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
            else:
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                      city,
                                                                                                      rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patients vitals, condition, and lung sounds monitored throughout care, before and after all inteventions with no significant change.".format(
                        loc, ls, pc, ps, ass_text, ), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
    else:
        if exceptions_text == "":
            if mon == "5 lead":
                flash("Dispatch:", "h1")
                flash("{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                        city, rfd, age,
                                                                                                        au, sex, pf),
                      "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with {}".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash(name, "sig")
            elif mon == "12 lead":
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                      city, rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with {}".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash(name, "sig")
            else:
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                      city, rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patients vitals, condition, and lung sounds monitored throughout care, before and after all inteventions with {}".format(
                        loc, ls, pc, ps, ass_text, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash(name, "sig")
        else:
            if mon == "5 lead":
                flash("Dispatch:", "h1")
                flash("{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                        city,
                                                                                                        rfd, age, au,
                                                                                                        sex,
                                                                                                        pf), "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with {}".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
            elif mon == "12 lead":
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                      city,
                                                                                                      rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patient was placed on {} cardiac monitor to observe {}. Patients vitals, lung sounds, and cariac rhythm monitored throughout care, before and after all inteventions with {}".format(
                        loc, ls, pc, ps, ass_text, mon, rhythm, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
            else:
                flash("Dispatch:", "h1")
                flash(
                    "{} called to {}, {} for a {}. Arrived on scene to find a {} {} old {} {}".format(unit, address,
                                                                                                      city,
                                                                                                      rfd,
                                                                                                      age, au, sex, pf),
                    "dispatch")
                flash("Chief Complaint:", "h2")
                flash("{}".format(cc), "cc")
                flash("History of Present Illness", "h3")
                flash("{}".format(hpi), "hpi")
                flash("Assessment:", "h4")
                flash(
                    "Patient was {} with airway, breathing, and circulation intact. Skin was pink, warm, and dry. Lung{}. Pupils were {} at {}mm. Baseline vitals obtained. {} Patients vitals, condition, and lung sounds monitored throughout care, before and after all inteventions with {}.".format(
                        loc, ls, pc, ps, ass_text, changes_text), "assessment")
                flash("Treatment:", "h5")
                flash(treatment_text, "treatment")
                flash("Transport:", "h6")
                flash(
                    "The patient stated they did not want to be transported by ambulance at this time. We informed the patient of the {}, up to and including death. Patient {} at any time for if their condition changes or if they change their mind. Patient stated they understood. Patient {}".format(rof, callback, sign_refusal), "transport")
                flash("Exceptions:", "h7")
                flash(exceptions_text, "exceptions")
                flash(name, "sig")
    return render_template("rgenerator.html")

if __name__ == '__main__':
    app.run()

