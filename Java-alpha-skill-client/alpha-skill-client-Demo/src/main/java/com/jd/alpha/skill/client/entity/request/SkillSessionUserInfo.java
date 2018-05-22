package com.jd.alpha.skill.client.entity.request;

import lombok.*;

/**
 * Skill Session 用户信息
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 16:11 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SkillSessionUserInfo {
    /**
     * 用户ID
     */
    private String userId;

    /**
     * 授权Token
     */
    private String accessToken;
    
}
