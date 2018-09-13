package com.jd.alpha.skill.client;

import com.jd.alpha.skill.client.constant.IntentTypeConstants;
import com.jd.alpha.skill.client.constant.RequestTypeConstants;
import com.jd.alpha.skill.client.entity.request.SkillData;
import com.jd.alpha.skill.client.entity.response.SkillResponse;

/**
 * Handler 处理类
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2018/1/8 1:51 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
public abstract class RequestHandler {

    public SkillResponse handle(SkillData skillData) {
        try {
            if (!validate(skillData)) {
                return SkillResponse.builder().shouldEndSession(true).build();
            }

            if (skillData.getSession().isNew()) {
                onSessionStarted(skillData);
            }

            String requestType = skillData.getRequest().getType();

            switch (requestType) {
                case RequestTypeConstants.LAUNCH_REQUEST:
                    return onLaunchRequest(skillData);
                case RequestTypeConstants.INTENT_REQUEST:
                    return handleIntentRequest(skillData);
                case RequestTypeConstants.SESSION_END_REQUEST:
                    onSessionEndedRequest(skillData);
                    break;
                default:
                    return defaultResponse(skillData);
            }
            return SkillResponse.builder().shouldEndSession(true).build();
        } catch (Exception e) {
            return SkillResponse.builder().shouldEndSession(true).build();
        }
    }

    public SkillResponse handleIntentRequest(SkillData skillData) {
        String intentName = skillData.getRequest().getIntent().getName();

        if (!intentName.startsWith("Alpha.")) {
            return onIntentRequest(skillData);
        }

        if (IntentTypeConstants.CANCEL_INTENT.equalsIgnoreCase(intentName)) {
            return onCancelIntent(skillData);
        }

        if (IntentTypeConstants.HELP_INTENT.equalsIgnoreCase(intentName)) {
            return onHelpIntent(skillData);
        }

        if (IntentTypeConstants.NEXT_INTENT.equalsIgnoreCase(intentName)) {
            return onNextIntent(skillData);
        }

        if (IntentTypeConstants.REPEAT_INTENT.equalsIgnoreCase(intentName)) {
            return onRepeatIntent(skillData);
        }

        return onOtherBuildInIntent(skillData);
    }

    public abstract boolean validate(SkillData skillData);

    public abstract void onSessionStarted(SkillData skillData);

    public abstract SkillResponse onLaunchRequest(SkillData skillData);

    public abstract SkillResponse onIntentRequest(SkillData skillData);

    public abstract void onSessionEndedRequest(SkillData skillData);

    public abstract SkillResponse onCancelIntent(SkillData skillData);

    public abstract SkillResponse onHelpIntent(SkillData skillData);

    public abstract SkillResponse onNextIntent(SkillData skillData);

    public abstract SkillResponse onRepeatIntent(SkillData skillData);

    public abstract SkillResponse onOtherBuildInIntent(SkillData skillData);

    public abstract SkillResponse defaultResponse(SkillData skillData);

}
