# 🚀 Emoji Expander Bot

A powerful Telegram inline bot that expands emoji keywords into multiple emojis with support for both English and Persian languages, plus Persian number input.

**🤖 Bot**: [@emoji_expander_bot](https://t.me/emoji_expander_bot)

## ✨ Features

- 🔤 **Bilingual Support**: Works with both English and Persian keywords
- 🔢 **Persian Numbers**: Supports Persian numerals (۰۱۲۳۴۵۶۷۸۹)
- ⚡ **Inline Queries**: Use in any chat without adding the bot
- 🎯 **Smart Multiplication**: Repeat emojis any number of times
- 🌐 **Serverless**: Deployed on Vercel for fast response times

## 🎮 How to Use

### Basic Usage
Type `@emoji_expander_bot` followed by an emoji keyword in any Telegram chat:

```
@emoji_expander_bot smile
→ 😂

@emoji_expander_bot heart
→ ❤️
```

### Multiply Emojis
Add a number after a dot to repeat emojis:

```
@emoji_expander_bot smile.5
→ 😂😂😂😂😂

@emoji_expander_bot fire.10
→ 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
```

### Persian Support
Works with Persian keywords and numbers:

```
@emoji_expander_bot خنده.۵
→ 😂😂😂😂😂

@emoji_expander_bot قلب.۳
→ ❤️❤️❤️
```

## 📋 Supported Emojis

### 😊 Happy/Positive
| English | Persian | Emoji |
|---------|---------|-------|
| `smile` | `خنده` | 😂 |
| `happy` | `خوشحال` | 😊 |
| `joy` | `شادی` | 😄 |
| `laugh` | `قهقهه` | 🤣 |
| `grin` | `پوزخند` | 😁 |

### 😢 Sad/Negative
| English | Persian | Emoji |
|---------|---------|-------|
| `sad` | `غمگین` | 🥲 |
| `cry` | `گریه` | 😢 |
| `tears` | `اشک` | 😭 |
| `disappointed` | `ناامید` | 😞 |
| `worried` | `نگران` | 😟 |

### ❤️ Love/Heart
| English | Persian | Emoji |
|---------|---------|-------|
| `heart` | `قلب` | ❤️ |
| `love` | `عشق` | 😍 |
| `kiss` | `بوس` | 😘 |
| `hearteyes` | `عاشق` | 😍 |

### 😠 Anger/Frustrated
| English | Persian | Emoji |
|---------|---------|-------|
| `angry` | `عصبانی` | 😠 |
| `rage` | `خشم` | 😡 |
| `mad` | `دیوانه` | 🤬 |

### 😲 Surprise/Shock
| English | Persian | Emoji |
|---------|---------|-------|
| `surprise` | `تعجب` | 😲 |
| `shock` | `شوک` | 😱 |
| `wow` | `واو` | 😮 |

### 😎 Cool/Confident
| English | Persian | Emoji |
|---------|---------|-------|
| `cool` | `باحال` | 😎 |
| `sunglasses` | `عینکی` | 😎 |
| `wink` | `چشمک` | 😉 |

### 🤔 Thinking/Confused
| English | Persian | Emoji |
|---------|---------|-------|
| `thinking` | `فکر` | 🤔 |
| `confused` | `گیج` | 😕 |

### 😴 Tired/Sick
| English | Persian | Emoji |
|---------|---------|-------|
| `tired` | `خسته` | 😴 |
| `sick` | `بیمار` | 🤒 |
| `fever` | `تب` | 🤒 |

### 👍 Gestures
| English | Persian | Emoji |
|---------|---------|-------|
| `thumbsup` | `لایک` | 👍 |
| `thumbsdown` | `دیسلایک` | 👎 |
| `ok` | `اوکی` | 👌 |
| `peace` | `صلح` | ✌️ |
| `clap` | `تشویق` | 👏 |

### 🔥 Objects
| English | Persian | Emoji |
|---------|---------|-------|
| `fire` | `آتش` | 🔥 |
| `star` | `ستاره` | ⭐ |
| `moon` | `ماه` | 🌙 |
| `sun` | `خورشید` | ☀️ |

### ⚽ Sports
| English | Persian | Emoji |
|---------|---------|-------|
| `football` | `فوتبال` | ⚽ |
| `basketball` | `بسکتبال` | 🏀 |

### 🌧️ Weather
| English | Persian | Emoji |
|---------|---------|-------|
| `rain` | `باران` | 🌧️ |
| `snow` | `برف` | ❄️ |
| `thunder` | `رعد` | ⛈️ |

### 🎉 Party/Celebration
| English | Persian | Emoji |
|---------|---------|-------|
| `party` | `جشن` | 🎉 |
| `cake` | `کیک` | 🎂 |
| `gift` | `هدیه` | 🎁 |

### 📱 Technology
| English | Persian | Emoji |
|---------|---------|-------|
| `phone` | `تلفن` | 📱 |
| `computer` | `کامپیوتر` | 💻 |

### 💰 Money
| English | Persian | Emoji |
|---------|---------|-------|
| `money` | `پول` | 💰 |
| `dollar` | `دلار` | 💵 |

### 🕐 Time
| English | Persian | Emoji |
|---------|---------|-------|
| `clock` | `ساعت` | 🕐 |

### 🚗 Transportation
| English | Persian | Emoji |
|---------|---------|-------|
| `car` | `ماشین` | 🚗 |
| `plane` | `هواپیما` | ✈️ |

### 🌸 Flowers/Nature
| English | Persian | Emoji |
|---------|---------|-------|
| `flower` | `گل` | 🌸 |
| `rose` | `رز` | 🌹 |
| `tree` | `درخت` | 🌳 |

## 🛠️ Technical Details

### Built With
- **Framework**: [grammY](https://grammy.dev/) - Modern Telegram Bot Framework
- **Runtime**: Node.js with TypeScript
- **Deployment**: [Vercel](https://vercel.com/) Serverless Functions
- **Template**: Based on [grammy-vercel-boilerplate](https://github.com/neumanf/grammy-vercel-boilerplate)

### Features
- **Persian Number Processing**: Converts Persian numerals (۰۱۲۳۴۵۶۷۸۹) to English for processing
- **Optimized Parsing**: Direct character code conversion without string replacement
- **Serverless Architecture**: Fast cold starts and automatic scaling
- **Inline Query Support**: Works in any chat without adding the bot

## 🚀 Deploy Your Own

### Prerequisites
1. Create a bot with [@BotFather](https://t.me/BotFather)
2. Get your bot token
3. Enable inline mode with `/setinline` command

### Quick Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/emoji-expander-bot)

### Manual Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/emoji-expander-bot
   cd emoji-expander-bot
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your BOT_TOKEN
   ```

4. **Deploy to Vercel**
   ```bash
   npm install -g vercel
   vercel --prod
   ```

5. **Set webhook**
   ```bash
   # Replace YOUR_BOT_TOKEN and YOUR_VERCEL_URL
   curl "https://api.telegram.org/botYOUR_BOT_TOKEN/setWebhook?url=YOUR_VERCEL_URL/api/webhook"
   ```

6. **Enable inline mode**
   - Send `/setinline` to @BotFather
   - Select your bot
   - Set placeholder text

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Your Telegram bot token from @BotFather | ✅ |

## 📝 Examples

### English Examples
```
@emoji_expander_bot happy.3    → 😊😊😊
@emoji_expander_bot fire.7     → 🔥🔥🔥🔥🔥🔥🔥
@emoji_expander_bot party.2    → 🎉🎉
```

### Persian Examples
```
@emoji_expander_bot خنده.۵     → 😂😂😂😂😂
@emoji_expander_bot قلب.۱۰     → ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
@emoji_expander_bot آتش.۳      → 🔥🔥🔥
```

### Mixed Examples
```
@emoji_expander_bot smile.۴    → 😂😂😂😂
@emoji_expander_bot ماه.5      → 🌙🌙🌙🌙🌙
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Adding New Emojis
1. Edit `src/core/bot/index.ts`
2. Add your emoji to the `emojies` object
3. Update this README
4. Submit a PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Bot**: [@emoji_expander_bot](https://t.me/emoji_expander_bot)
- **Telegram Bot API**: [Documentation](https://core.telegram.org/bots/api)
- **grammY Framework**: [Website](https://grammy.dev/)
- **Vercel**: [Platform](https://vercel.com/)

## 🙏 Acknowledgments

- [grammY](https://grammy.dev/) for the excellent Telegram bot framework
- [neumanf](https://github.com/neumanf) for the Vercel boilerplate
- [Vercel](https://vercel.com/) for the serverless platform

---

<div align="center">
  <strong>Made with ❤️ for the Telegram community</strong>
</div>
