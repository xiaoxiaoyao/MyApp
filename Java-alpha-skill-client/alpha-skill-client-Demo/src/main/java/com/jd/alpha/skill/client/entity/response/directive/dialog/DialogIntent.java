package com.jd.alpha.skill.client.entity.response.directive.dialog;

import lombok.*;

import java.util.Map;

/**
 * 类描述
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 17:28 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class DialogIntent {

    private String name;

    private String confirmResult;

    private Map<String, DialogSlot> slots;

}