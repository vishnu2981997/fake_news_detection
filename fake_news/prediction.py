from sklearn import model_selection
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from . import views


def predict(article):
    test = article
    pickle_in = open('fake_news\\trained_classifiers.pickle', 'rb')
    cv = CountVectorizer(stop_words='english')
    x_traincv = cv.fit_transform(pickle.load(pickle_in))
    X_test = pickle.load(pickle_in)
    x_testcv = cv.transform(X_test)

    y_test = pickle.load(pickle_in)
    mnb2 = pickle.load(pickle_in)
    rf = pickle.load(pickle_in)
    decision = pickle.load(pickle_in)
    svm = pickle.load(pickle_in)
    knn = pickle.load(pickle_in)

    # s = """the final stretch of the election, Hillary Rodham Clinton has gone to war with the FBI. But that’s exactly what Hillary and her people have done. Coma patients just waking up now and watching an hour of CNN from their hospital beds would assume that FBI Director James Comey is Hillary’s opponent in this election. The FBI’s leadership is being warned that the entire left-wing establishment will form a lynch mob if they continue going after Hillary. And the FBI’s credibility is being attacked by the media and the Democrats to preemptively head off the results of the investigation of the Clinton Foundation and Hillary Clinton. The New York Times has compared Comey to J. Edgar Hoover. Its bizarre headline, “James Comey Role Recalls Hoover’s FBI, Fairly or Not” practically admits up front that it’s spouting nonsense. The Boston Globe has published a column calling for Comey’s resignation. Not to be outdone, Time has an editorial claiming that the scandal is really an attack on all women. Countless media stories charge Comey with violating procedure. Do you know what’s a procedural violation? Emailing classified information stored on your bathroom server. If James Comey is really out to hurt Hillary, he picked one hell of a strange way to do it. Either Comey is the most cunning FBI director that ever lived or he’s just awkwardly trying to navigate a political mess that has trapped him between a DOJ leadership whose political futures are tied to Hillary’s victory and his own bureau whose apolitical agents just want to be allowed to do their jobs. And it’s an interesting question. Pretending that nothing was wrong was a bad strategy, but it was a better one that picking a fight with the FBI while lunatic Clinton associates try to claim that the FBI is really the KGB. Hillary Clinton might be arrogant enough to lash out at the FBI now that she believes that victory is near. The same kind of hubris that led her to plan her victory fireworks display could lead her to declare a war on the FBI for irritating her during the final miles of her campaign. Going to war with the FBI is not the behavior of a smart and focused presidential campaign. It’s an act of desperation. When a presidential candidate decides that her only option is to try and destroy the credibility of the FBI, that’s not hubris, it’s fear of what the FBI might be about to reveal about her. There’s only one reason for such bizarre behavior. Clinton loyalists rigged the old investigation. They knew the outcome ahead of time as well as they knew the debate questions. Now suddenly they are no longer in control. And they are afraid. The FBI has wiretaps from the investigation of the Clinton Foundation. It’s finding new emails all the time. And Clintonworld panicked. The spinmeisters of Clintonworld have claimed that the email scandal is just so much smoke without fire. All that’s here is the appearance of impropriety without any of the substance. But this isn’t how you react to smoke. It’s how you respond to a fire. The Clintons have weathered countless scandals over the years. Whatever they are protecting this time around is bigger than the usual corruption, bribery, sexual assaults and abuses of power that have followed them around throughout the years. This is bigger and more damaging than any of the allegations that have already come out. And they don’t want FBI investigators anywhere near it. Hillary Clinton has awkwardly wound her way through numerous scandals in just this election cycle. But she’s never shown fear or desperation before. Now that has changed. Whatever she is afraid of, it lies buried in her emails with Huma Abedin. And it can bring her down like nothing else has."""

    x = cv.transform(np.asarray([test]))
    mnb2pred = "FAKE" if mnb2.predict(x) == 0 else "REAL"
    rfpred = "FAKE" if rf.predict(x) == 0 else "REAL"
    decisionpred = "FAKE" if decision.predict(x) == 0 else "REAL"
    svmpred = "FAKE" if svm.predict(x) == 0 else "REAL"
    knnpred = "FAKE" if knn.predict(x) == 0 else "REAL"

    c = [mnb2pred, rfpred, decisionpred, svmpred, knnpred]

    if c.count("REAL") >= 3:
        hybrid = "REAl"

    else:
        hybrid = "FAKE"
    pickle_in.close()
    return [mnb2pred, rfpred, decisionpred, svmpred, knnpred, hybrid]
