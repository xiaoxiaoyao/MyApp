package com.jd.alpha.skill.client.entity.request;

import lombok.*;

import java.util.Map;

/**
 * Skill Session
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 15:43 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SkillSession {

    /**
     * 是否为新会话
     */
    private boolean isNew;

    /**
     * 全局唯一标识
     */
    private String sessionId;

    /**
     * 用户信息
     */
    private SkillSessionUserInfo user;

    /**
     * 设备信息
     */
    private SkillSessionDeviceInfo device;

    /**
     * 应用信息
     */
    private SkillSessionApplicationInfo application;

    /**
     * 上下文信息
     */
    private Map<String, String> contexts;

}
